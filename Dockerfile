FROM python
COPY requirements.txt .
COPY validator.py .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["validator.py"]
