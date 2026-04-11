@echo off
title Water Quality ML Project
echo ====================================
echo Starting Water Quality Project...
echo ====================================

cd /d %~dp0

echo.
echo Training Model...
cd model
python train_model.py

echo.
echo Starting Streamlit App...
cd ../app
streamlit run app.py

pause