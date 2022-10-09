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
