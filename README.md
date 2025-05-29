# Plantae.A

#This is our deployed link :- https://plantae-ai.vercel.app/

Plantae.Ai is an AI-powered agricultural assistant designed to help farmers and plantation managers monitor crop health, count trees, and detect weeds efficiently using advanced AI models.

---

## Features

### 1. Disease Diagnosis  
- Users can upload photos of crop leaves.  
- Our AI model (trained on 38 disease classes using the [PlantVillage dataset](https://github.com/spMohanty/PlantVillage-Dataset)) instantly identifies diseases.  
- Prototype achieves ~92% accuracy on tomato leaf disease classification ([Research Reference](https://www.researchgate.net/)).  
- The app provides the predicted disease along with recommended actions.

### 2. Tree Counting  
- Processes aerial or satellite images to automatically count trees such as coconut or orchard trees.  
- Eliminates the need for manual surveys, speeding up plantation monitoring.  
- Displays detected trees on a map interface with total counts ([Inspired by Flypix.ai](https://flypix.ai) and [Medium](https://medium.com/)).

### 3. Weed Detection  
- Real-time weed detection using live camera feed.  
- Highlights each weed plant for precise targeting with >90% accuracy ([Reference](https://keymakr.com/)).  
- Enables spot treatment to reduce herbicide use and environmental impact.

---

## Tech Stack

- **Frontend:** Next.js, React.js, Tailwind CSS  
- **Backend:** Flask and FastAPI (Python) serving REST APIs  
- **ML Framework:** TensorFlow/Keras  
- **Model Training:** ~54,000 images from PlantVillage dataset (38 classes)  
- **Server:** Uvicorn to run FastAPI backend  

---

## Getting Started

### Frontend

1. Navigate to the frontend directory:  
   ```bash
   cd frontend
Install dependencies and start the development server:

npm install
npm run dev

Open http://localhost:3000 in your browser.

Upload images and click the buttons to use features like Disease Detection, Tree Counting, and Weed Detection.

Backend
Ensure Python and required packages are installed (Flask, FastAPI, TensorFlow, etc.).

Run the backend server using Uvicorn:

uvicorn main:app --reload
Backend API serves model inference requests from the frontend.

Models are trained on 38 classes using the PlantVillage dataset (~54K images).

