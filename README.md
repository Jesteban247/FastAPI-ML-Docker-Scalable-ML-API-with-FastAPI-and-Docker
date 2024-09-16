# 🚀 FastAPI-ML-Docker: Scalable ML API with FastAPI and Docker

Welcome to the **FastAPI-ML-Docker** project! 🌟 This project demonstrates how to build a scalable machine learning API using FastAPI and Docker. It leverages the powerful BLIP model for image captioning to generate captions for images you upload. 📸📝

## 🧩 Model Used

We are using the [BLIP Image Captioning Model](https://huggingface.co/Salesforce/blip-image-captioning-large) from Salesforce. This model generates high-quality captions for images, making it a great choice for various applications. 🤖✨

## 🎥 Project Demo

https://github.com/user-attachments/assets/0e3e7498-de68-47da-86b0-9d811391d107

## 🚀 Running the Project

To run the project, use the following command:

```bash
docker compose up --build
```

This command builds the Docker image and starts the container. Your FastAPI application will be available at `http://localhost:8000`.

## 📝 Acknowledgements

Special thanks to the guide and inspiration from this [YouTube video](https://www.youtube.com/watch?v=iqrS7Q174Ac). 🙌

## 📚 Dependencies

- FastAPI 🌐
- Uvicorn 🚀
- Pillow 🖼️
- Transformers 🤗
- Docker 🐳

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
