FROM python:3.12 slim AS build
ADD . /pythonapp      
WORKDIR /pythonapp
RUN pip install --prefix=/devops -r requirements.txt

FROM python:3.12 slim AS runtime
LABEL project="pythonproject"
LABEL author="devopsteam"
COPY --from=build /pythonapp/devops/aws
WORKDIR /aws
EXPOSE 5001
CMD ["python3","app.py"]
                            