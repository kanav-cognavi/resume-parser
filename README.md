clone the repo
git clone https://github.com/kanav-cognavi/resume-parser.git


create virtual env
  python3 -m venv env
  
activate virtual env
  source bin activate
  
cd resume-parse  
install all packages: pip3 install -r requirements.txt

#make sure to add open api key in code

#run this command to run server
streamlit run main.py and now goto http://localhost:8501

reference: https://python.langchain.com/docs/modules/model_io/output_parsers/quick_start
