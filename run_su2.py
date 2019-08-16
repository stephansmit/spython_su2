import os
from spython.main import Client as client
import requests


def download_testcase(testcase_dir):
    try:
        os.mkdir(testcase_dir)
    except:
        pass
    
    urls = [
    	'https://raw.githubusercontent.com/su2code/SU2/develop/TestCases/turbomachinery/APU_turbocharger/Jones.cfg',
    	'https://github.com/su2code/SU2/raw/develop/TestCases/turbomachinery/APU_turbocharger/stator.cfg',
    	'https://github.com/su2code/SU2/raw/develop/TestCases/turbomachinery/APU_turbocharger/rotor.cfg',
    	'https://github.com/su2code/TestCases/raw/develop/turbomachinery/APU_turbocharger/mesh_jones_turbine.su2'
            ]
    
    for url in urls:
        r = requests.get(url)
        with open(os.path.join(testcase_dir,url.split('/')[-1]), 'wb') as f:
                f.write(r.content)
    
def download_images(image_dir, image_url):
    image_name='su2_containers_fork_dev.sif'
    try:
        os.mkdir(image_dir)
    except:
        pass
    
    client.pull(image=image_url,name=image_name, pull_folder=image_dir)
    return image_name

def run_case(image_dir, image_name, testcase_dir):
    client.load(os.path.join(image_dir,image_name))
    output = client.execute(['mpirun', '-np', '6', '/SU2/bin/SU2_CFD','Jones.cfg'], bind=testcase_dir+":/data:", options=['--pwd','/data'], stream=True)
    for val in output:
        print(val.strip('\n'))

if __name__=="__main__":
    testcase_dir = 'testcase/'
    image_dir='images/'
    image_url='shub://stephansmit/su2_containers:fork_dev'
    print("Downloading the testcase")
    download_testcase(testcase_dir)
    print("Downloading the Singularity Images")
    image_name = download_images(image_dir,image_url)
    print("Running the case")
    run_case(image_dir,image_name,testcase_dir)
