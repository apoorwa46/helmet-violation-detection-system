python training\train_model.py
(venv) PS D:\Personal Projects\Helmet Detection> python training\train_model.py
New https://pypi.org/project/ultralytics/8.4.66 available  Update with 'pip install -U ultralytics'
Ultralytics 8.4.61  Python-3.12.5 torch-2.12.0+cpu CPU (12th Gen Intel Core i7-12650H)
engine\trainer: agnostic_nms=False, amp=True, angle=1.0, augment=False, auto_augment=randaugment, batch=16, bgr=0.0, box=7.5, cache=False, cfg=None, classes=None, close_mosaic=10, cls=0.5, cls_pw=0.0, compile=False, conf=None, copy_paste=0.0, copy_paste_mode=flip, cos_lr=False, cutmix=0.0, data=datasets/processed/data.yaml, degrees=0.0, deterministic=True, device=cpu, dfl=1.5, dnn=False, dropout=0.0, dynamic=False, embed=None, end2end=None, epochs=50, erasing=0.4, exist_ok=False, fliplr=0.5, flipud=0.0, format=torchscript, fraction=1.0, freeze=None, half=False, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, imgsz=640, int8=False, iou=0.7, keras=False, kobj=1.0, line_width=None, lr0=0.01, lrf=0.01, mask_ratio=4, max_det=300, mixup=0.0, mode=train, model=yolov8n.pt, momentum=0.937, mosaic=1.0, multi_scale=0.0, name=helmet_training, nbs=64, nms=False, opset=None, optimize=False, optimizer=auto, overlap_mask=True, patience=10, perspective=0.0, plots=True, pose=12.0, pretrained=True, profile=False, project=runs, rect=False, resume=False, retina_masks=False, rle=1.0, save=True, save_conf=False, save_crop=False, save_dir=D:\Personal Projects\Helmet Detection\runs\detect\runs\helmet_training, save_frames=False, save_json=False, save_period=-1, save_txt=False, scale=0.5, seed=0, shear=0.0, show=False, show_boxes=True, show_conf=True, show_labels=True, simplify=True, single_cls=False, source=None, split=val, stream_buffer=False, task=detect, time=None, tracker=botsort.yaml, translate=0.1, val=True, verbose=True, vid_stride=1, visualize=False, warmup_bias_lr=0.1, warmup_epochs=3.0, warmup_momentum=0.8, weight_decay=0.0005, workers=8, workspace=None
Downloading https://ultralytics.com/assets/Arial.ttf to 'C:\Users\apoor\AppData\Roaming\Ultralytics\Arial.ttf': 64% ━━━━━━━╸──── 480.0/755.1KB 4.6MB/s 0.
Downloading https://ultralytics.com/assets/Arial.ttf to 'C:\Users\apoor\AppData\Roaming\Ultralytics\Arial.ttf': 100% ━━━━━━━━━━━━ 755.1KB 5.1MB/s 0.1s
Overriding model.yaml nc=80 with nc=2

                   from  n    params  module                                       arguments                     
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                
  2                  -1  1      7360  ultralytics.nn.modules.block.C2f             [32, 32, 1, True]             
  3                  -1  1     18560  ultralytics.nn.modules.conv.Conv             [32, 64, 3, 2]                
  4                  -1  2     49664  ultralytics.nn.modules.block.C2f             [64, 64, 2, True]             
  5                  -1  1     73984  ultralytics.nn.modules.conv.Conv             [64, 128, 3, 2]               
  6                  -1  2    197632  ultralytics.nn.modules.block.C2f             [128, 128, 2, True]           
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  8                  -1  1    460288  ultralytics.nn.modules.block.C2f             [256, 256, 1, True]           
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 
 10                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 11             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 12                  -1  1    148224  ultralytics.nn.modules.block.C2f             [384, 128, 1]                 
 13                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 14             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 15                  -1  1     37248  ultralytics.nn.modules.block.C2f             [192, 64, 1]                  
 16                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 17            [-1, 12]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 18                  -1  1    123648  ultralytics.nn.modules.block.C2f             [192, 128, 1]                 
 19                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 20             [-1, 9]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 21                  -1  1    493056  ultralytics.nn.modules.block.C2f             [384, 256, 1]                 
 22        [15, 18, 21]  1    751702  ultralytics.nn.modules.head.Detect           [2, 16, None, [64, 128, 256]] 
Model summary: 130 layers, 3,011,238 parameters, 3,011,222 gradients, 8.2 GFLOPs

Transferred 319/355 items from pretrained weights
Freezing layer 'model.22.dfl.conv.weight'
train: Fast image access  (ping: 0.10.0 ms, read: 68.810.6 MB/s, size: 632.7 KB)
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 21 images, 0 backgrounds, 0 corrupt: 4% ──────────── 21/534 60.6
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 58 images, 0 backgrounds, 1 corrupt: 11% ━─────────── 58/534 152
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 84 images, 0 backgrounds, 2 corrupt: 16% ━╸────────── 84/534 183
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 121 images, 0 backgrounds, 2 corrupt: 23% ━━╸───────── 121/534 2
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 157 images, 0 backgrounds, 3 corrupt: 29% ━━━╸──────── 157/534 2
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 188 images, 0 backgrounds, 4 corrupt: 35% ━━━━──────── 188/534 2
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 226 images, 1 backgrounds, 4 corrupt: 42% ━━━━━─────── 226/534 2
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 263 images, 1 backgrounds, 4 corrupt: 49% ━━━━━╸────── 263/534 2
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 308 images, 2 backgrounds, 6 corrupt: 58% ━━━━━━╸───── 308/534 3
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 343 images, 2 backgrounds, 6 corrupt: 64% ━━━━━━━╸──── 343/534 3
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 382 images, 2 backgrounds, 6 corrupt: 72% ━━━━━━━━╸─── 382/534 3
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 417 images, 2 backgrounds, 7 corrupt: 78% ━━━━━━━━━─── 417/534 3
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 455 images, 2 backgrounds, 8 corrupt: 85% ━━━━━━━━━━── 455/534 3
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 487 images, 2 backgrounds, 9 corrupt: 91% ━━━━━━━━━━╸─ 487/534 3
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 525 images, 2 backgrounds, 11 corrupt: 98% ━━━━━━━━━━━╸ 525/534 
train: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\train\labels... 534 images, 2 backgrounds, 11 corrupt: 100% ━━━━━━━━━━━━ 534/534 331.3it/s 1.6s
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets140.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [547.685  84.5   132.165 151.   ]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets205.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [263.5  43.   85.   74. ]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets279.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [194.5  56.  103.  100. ]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets343.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [682.27 150.5  118.22 107.  ]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets441.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [310.5  41.5  61.   63. ]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets444.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [299.  48.  78.  80.]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets616.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [750.  297.5  68.   91. ]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets671.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [863. 251.  52.  52.]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets706.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [379.5  82.5  61.   65. ]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets75.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [471.  290.5  82.  109.  761.  291.5  84.   97.  466.5 297.  109.  118. ]
train: D:\Personal Projects\Helmet Detection\datasets\processed\train\images\BikesHelmets80.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [424.5      45.29778  71.       82.63111]
train: New cache created: D:\Personal Projects\Helmet Detection\datasets\processed\train\labels.cache
val: Fast image access  (ping: 0.20.1 ms, read: 72.111.8 MB/s, size: 675.7 KB)
val: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\valid\labels... 30 images, 0 backgrounds, 0 corrupt: 20% ━━────────── 30/152 84.7i
val: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\valid\labels... 63 images, 0 backgrounds, 1 corrupt: 41% ━━━━╸─────── 63/152 157.8
val: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\valid\labels... 97 images, 0 backgrounds, 2 corrupt: 64% ━━━━━━━╸──── 97/152 210.7
val: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\valid\labels... 129 images, 0 backgrounds, 2 corrupt: 85% ━━━━━━━━━━── 129/152 240
val: Scanning D:\Personal Projects\Helmet Detection\datasets\processed\valid\labels... 152 images, 1 backgrounds, 3 corrupt: 100% ━━━━━━━━━━━━ 152/152 331.3it/s 0.5s
val: D:\Personal Projects\Helmet Detection\datasets\processed\valid\images\BikesHelmets326.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [157.   56.5  86.   97. ]
val: D:\Personal Projects\Helmet Detection\datasets\processed\valid\images\BikesHelmets530.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [313.3525  74.     102.115  116.    ]
val: D:\Personal Projects\Helmet Detection\datasets\processed\valid\images\BikesHelmets764.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [219.  91.  80.  82.]
val: New cache created: D:\Personal Projects\Helmet Detection\datasets\processed\valid\labels.cache
optimizer: 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically... 
optimizer: AdamW(lr=0.001667, momentum=0.9) with parameter groups 57 weight(decay=0.0), 64 weight(decay=0.0005), 63 bias(decay=0.0)
Plotting labels to D:\Personal Projects\Helmet Detection\runs\detect\runs\helmet_training\labels.jpg... 
Image sizes 640 train, 640 val
Using 0 dataloader workers
Logging results to D:\Personal Projects\Helmet Detection\runs\detect\runs\helmet_training
Starting training for 50 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       1/50         0G      1.479      2.787      1.222         11        640: 100% ━━━━━━━━━━━━ 33/33 7.2s/it 3:57
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 2.0s/it 10.0s
                   all        149        258    0.00604      0.942      0.353      0.182

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       2/50         0G      1.392      1.891      1.159         11        640: 100% ━━━━━━━━━━━━ 33/33 6.9s/it 3:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.4s/it 21.9s
                   all        149        258      0.622      0.274      0.388       0.22

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       3/50         0G      1.441      1.669      1.194         11        640: 100% ━━━━━━━━━━━━ 33/33 6.8s/it 3:43
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.9s/it 24.7s
                   all        149        258      0.727      0.192      0.163     0.0966

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       4/50         0G      1.385      1.531      1.193         11        640: 100% ━━━━━━━━━━━━ 33/33 8.5s/it 4:42
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 5.0s/it 25.0s
                   all        149        258      0.497      0.555      0.496      0.281

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       5/50         0G      1.411       1.48      1.187         11        640: 100% ━━━━━━━━━━━━ 33/33 8.7s/it 4:46
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.8s/it 23.9s
                   all        149        258      0.595      0.643      0.598      0.324

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       6/50         0G      1.359      1.326      1.156         11        640: 100% ━━━━━━━━━━━━ 33/33 8.7s/it 4:48
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.8s/it 23.9s
                   all        149        258       0.62      0.677      0.659      0.386

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       7/50         0G      1.399      1.313      1.172         11        640: 100% ━━━━━━━━━━━━ 33/33 8.7s/it 4:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.8s/it 24.1s
                   all        149        258      0.607      0.704      0.662      0.379

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       8/50         0G      1.387      1.233       1.16         11        640: 100% ━━━━━━━━━━━━ 33/33 8.7s/it 4:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.7s/it 23.7s
                   all        149        258       0.64      0.601      0.607      0.357

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       9/50         0G      1.341      1.179      1.152         11        640: 100% ━━━━━━━━━━━━ 33/33 8.6s/it 4:45
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.7s/it 23.6s
                   all        149        258      0.704      0.635      0.671       0.39

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      10/50         0G      1.323      1.105      1.163         11        640: 100% ━━━━━━━━━━━━ 33/33 8.7s/it 4:47
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.9s/it 24.6s
                   all        149        258      0.733      0.694      0.717      0.415

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      11/50         0G      1.301       1.08      1.154         11        640: 100% ━━━━━━━━━━━━ 33/33 8.7s/it 4:46
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 1.9s/it 9.4s
                   all        149        258      0.662      0.695      0.704      0.448

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      12/50         0G      1.285      1.025      1.118         11        640: 100% ━━━━━━━━━━━━ 33/33 3.2s/it 1:46
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 1.8s/it 9.0s
                   all        149        258      0.546      0.703      0.569      0.341

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      13/50         0G      1.289     0.9813      1.133         11        640: 100% ━━━━━━━━━━━━ 33/33 3.2s/it 1:46
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 1.9s/it 9.4s
                   all        149        258      0.692      0.677      0.708      0.418

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      14/50         0G      1.295     0.9857      1.123         11        640: 100% ━━━━━━━━━━━━ 33/33 7.0s/it 3:50
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.6s/it 23.2s
                   all        149        258      0.671      0.755      0.726       0.44

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      15/50         0G      1.266     0.9639      1.111         11        640: 100% ━━━━━━━━━━━━ 33/33 8.1s/it 4:27
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.6s/it 23.2s
                   all        149        258      0.638      0.758      0.686      0.384

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      16/50         0G      1.291     0.9805      1.129         11        640: 100% ━━━━━━━━━━━━ 33/33 8.4s/it 4:38
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.5s/it 22.6s
                   all        149        258      0.701      0.753      0.736       0.44

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      17/50         0G      1.264     0.9065      1.096         11        640: 100% ━━━━━━━━━━━━ 33/33 8.4s/it 4:39
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.5s/it 22.7s
                   all        149        258      0.729      0.668      0.713      0.434

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      18/50         0G      1.243     0.9061      1.095         11        640: 100% ━━━━━━━━━━━━ 33/33 8.4s/it 4:38
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.5s/it 22.7s
                   all        149        258      0.726      0.678      0.662      0.387

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      19/50         0G      1.213     0.8432      1.088         11        640: 100% ━━━━━━━━━━━━ 33/33 8.5s/it 4:40
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.5s/it 22.6s
                   all        149        258      0.701      0.661      0.637      0.377

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      20/50         0G        1.2     0.8427      1.104         11        640: 100% ━━━━━━━━━━━━ 33/33 8.4s/it 4:37
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.6s/it 22.9s
                   all        149        258      0.709      0.688      0.711      0.419

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      21/50         0G      1.238     0.8498      1.094         11        640: 100% ━━━━━━━━━━━━ 33/33 8.4s/it 4:38
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.7s/it 23.7s
                   all        149        258      0.645      0.688      0.666      0.388
EarlyStopping: Training stopped early as no improvement observed in last 10 epochs. Best results observed at epoch 11, best model saved as best.pt.
To update EarlyStopping(patience=10) pass a new patience value, i.e. `patience=300` or use `patience=0` to disable EarlyStopping.

21 epochs completed in 1.611 hours.
Optimizer stripped from D:\Personal Projects\Helmet Detection\runs\detect\runs\helmet_training\weights\last.pt, 6.2MB
Optimizer stripped from D:\Personal Projects\Helmet Detection\runs\detect\runs\helmet_training\weights\best.pt, 6.2MB

Validating D:\Personal Projects\Helmet Detection\runs\detect\runs\helmet_training\weights\best.pt...
Ultralytics 8.4.61  Python-3.12.5 torch-2.12.0+cpu CPU (12th Gen Intel Core i7-12650H)
Model summary (fused): 73 layers, 3,006,038 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 5/5 4.1s/it 20.4s
                   all        149        258      0.662      0.695      0.704      0.448
           With Helmet        111        198       0.73      0.903      0.868      0.572
        Without Helmet         43         60      0.594      0.487       0.54      0.324
Speed: 1.2ms preprocess, 114.0ms inference, 0.0ms loss, 0.8ms postprocess per image
Results saved to D:\Personal Projects\Helmet Detection\runs\detect\runs\helmet_training
Training Complete
