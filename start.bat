@echo off
cd /d "C:\python\"
"C:\Python313\python.exe" -m streamlit run app.py --server.address=0.0.0.0 --server.port=8501
pause