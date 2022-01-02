import cv2
import os

present=os.getcwd()

def cam(name,ran,back):
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Cam")

    img_counter = 0
    
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            os.chdir(back)
            break
        cv2.imshow("cam", frame)

        k = cv2.waitKey(1)
        
        if img_counter>=int(ran):
            os.chdir(back)
            break
        cv2.imshow("cam", frame)
            
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = f"{name}{img_counter}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            #print(f"{name} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

def train_real(name,back):
    print(f'\nDataset collecting at Train Real')
    ran=250
    w=f'{name}/train/real'
    now=os.path.join(w)
    os.chdir(now)
    cam(name,ran,back)
    os.chdir(back)

def train_spoof(name,back):
    print(f'Dataset collecting at Train Spoof')
    ran=250
    w=f'{name}/train/spoof'
    now=os.path.join(w)
    os.chdir(now)
    cam(name,ran,back)
    os.chdir(back)

def test_real(name,back):
    print(f'Dataset collecting at Test Real')
    ran=50
    w=f'{name}/test/real'
    now=os.path.join(w)
    os.chdir(now)
    cam(name,ran,back)
    os.chdir(back)
    
def test_spoof(name,back):
    print(f'Dataset collecting for Test Spoof')
    ran=50
    w=f'{name}/test/spoof'
    now=os.path.join(w)
    os.chdir(now)
    cam(name,ran,back)
    os.chdir(back)

def create():
    print('-----------WELCOME-----------\n')
    print('DEVOLOPER - VIRUPAKSHA GUPTHA\n')
    print('PLEASE COME INFRONT OF CAM')
    print('READY SET GET GO!.....\n')
    name=input('Enter person name: ')

    os.mkdir(name)

    os.makedirs(f'{name}/train')

    os.makedirs(f'{name}/test')

    present=os.getcwd()

    li=['train','test']
    lis=['real','spoof']

    for i in li:
        for j in lis:
            pa=os.path.join(name,i,j)
            os.makedirs(pa)
            
    train_real(name,present)
    test_real(name,present)
    train_spoof(name,present)
    test_spoof(name,present)
    
    print('\nTHANK YOU')
create()
