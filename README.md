<!-- GETTING STARTED -->

### Prerequisites

* python
* docker

### Installation and usage

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the project
```
git clone https://github.com/alimuteshov/parser.git
```
2. Go to project directory
```
cd parser
```
3. run
```
bash start.sh
```
4. run
```
docker build -t parser .
```
5. run
```
docker run --rm -v $(pwd):/usr/src/app -w /usr/src/app parser
```
