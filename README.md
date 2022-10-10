<!-- GETTING STARTED -->

### Prerequisites

* python
* docker

### Installation and usage

1. Clone the project
```
git clone https://github.com/alimuteshov/parser.git
```
2. Go to project directory
```
cd parser
```
3. Create data directory(all parsing results will be stored in this diectory)
```
bash start.sh
```
4. Build docker image
```
docker build -t parser .
```
5. run
```
docker run --rm -v $(pwd):/usr/src/app -w /usr/src/app parser
```

#### In order to use aggregation_app, you should install pandas, matplotlib and spacy.
You can do it by running 
```
bash aggregation_install.ssh
```
Examples:
When evaluating 1_task and 2_task you need to specify start and end dates.
```
python aggregation_app.py 1_task -s '2021-05' -e '2021-09'
```
```
python aggregation_app.py 2_task -s '2021-05' -e '2021-09'
```
```
python aggregation_app.py 3_task
```
