# 🌿 Disease Model API

This project provides an API to detect whether a plant leaf is **healthy (control)** or **diseased**, using **FastAPI** and a trained **CNN model**.

---

## 🚀 Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/disease_model_api.git
   cd disease_model_api
   ```

2. Create a virtual environment:
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the API:
   ```bash
   uvicorn main:app --reload
   ```

5. Open in browser: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ☁️ Deploying on Render

When creating a **Web Service** on [Render](https://render.com):

- **Build Command**
  ```bash
  pip install -r requirements.txt
  ```

- **Start Command**
  ```bash
  uvicorn main:app --host 0.0.0.0 --port 10000
  ```

⚠️ Ensure your trained model file (`model.pth`) is included in the repository.

---

## 📡 API Endpoints

- **GET /** → Health check  
- **POST /predict** → Upload an image and get prediction  

### Example (using curl)
```bash
curl -X POST "https://your-service-url.onrender.com/predict" -F "file=@leaf.jpg"
```

### Example Response
```json
{
  "class": "diseased",
  "confidence": 0.9823
}
```

---

## 📦 Project Structure
```
disease_model_api/
│── main.py
│── model.pth
│── requirements.txt
│── README.md
│── venv/ (ignored in .gitignore)
```

---

## 🛠 Tech Stack
- Python 3.x  
- FastAPI  
- PyTorch  
- Uvicorn  
- TorchVision  

---

## 👨‍💻 Author
Developed by **aqsa-sodagar**
