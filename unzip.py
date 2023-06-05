import os
import zipfile
import shutil

path = '/data/EPIC-KITCHENS/dataset/GroundTruth-SparseAnnotations/rgb_frames'
tasks = ['test', 'train', 'val']
tasks_path = [os.path.join(path, task) for task in tasks]



for task_path in tasks_path:
    videos = [v for v in os.listdir(task_path) if not v.endswith('.html')]
    for video in videos:
        vs = [v for v in os.listdir(os.path.join(task_path, video)) if not v.endswith('.html')]
        for zip in vs:
            if zip.endswith('.zip'):
                zip_path = os.path.join(task_path, video, zip)
                zip_ = zip.replace('.zip', '')
                if os.path.exists(os.path.join(task_path, video, zip_)):
                    shutil.rmtree(os.path.join(task_path, video, zip_))
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(os.path.join(task_path, video, zip_))
        print('2')

    print('1')