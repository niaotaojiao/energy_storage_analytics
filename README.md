# 儲能大數據分析計劃
* 介紹
* 專案架構
* 使用說明
* 文件

## 介紹
隨著綠能產業的快速發展，電池儲能技術在現代能源管理中扮演著不可或缺的角色，為可再生能源提供穩定的電力支持。隨著電池運行次數的增加，其電池的健康狀態（State of Health, SOH）會逐漸劣化，進而影響儲能系統的效能、安全性，甚至可能增加成本。對SOH進行精確預測有助於系統的維護和優化管理，避免因突發故障而引發的停機風險和經濟損失。因此，SOH的預測在電池管理系統（Battery Management System, BMS）中至關重要。 

本研究以人工智慧和雲端技術為基礎，旨在開發一個自動化的SOH預測模型，並將該模型部署至雲端，以建立一個精準、即時、可擴展的智能監測與預測系統。透過雲端部署的方式，該系統可以整合並分析來自不同電池的運行數據，進行全局性的健康狀態評估，為多場景應用提供可靠的數據支持和決策依據。除此之外，雲端的運算資源與存儲彈性使得模型更新與維護更加便捷，有利於長期的系統優化。 

## 專案架構
```
energy-bigdata-project/  
│  
├── data/                     # 請把資料放到這個文件夾下  
│   └── your data 
│  
├── models/                   # 訓練好的模型放這  
│   ├── soh_4k7k_0310.pt      
│   └── scaler.pkl        
│  
├── notebooks/                # Jupyter notebooks
│   ├── soh_darts.ipynb         
│   └── subsysten.ipynb    
│ 
├── vertex_docker/            # 自定模型部署的程式碼  
│   ├── app/                   
│   │   ├── models/
│   │   ├── app.py
│   │   └── opslib.py
│   ├── Dockerfile          
│   └── requirements.txt  
│  
├── vm_flaskapp/              # 在VM上的HTTP Server 
│   └── app.py                 
│ 
├── tests/                    # 測試相關目錄  
│   ├── test_cloud.py          
│   ├── test_docker.py       
│   └── test_flask.py              
│
├── README.md
└── .gitignore                
```

## 文件
- 完整開會記錄: [https://hackmd.io/@TzvQz1HOQ9GfhpT_zXxiGQ/BJwC3J36a](https://hackmd.io/@TzvQz1HOQ9GfhpT_zXxiGQ/BJwC3J36a)







