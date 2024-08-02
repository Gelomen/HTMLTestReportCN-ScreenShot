.PHONY: install freeze

# 安装依赖
install:
	pip3 install -r requirements.txt --break-system-packages

# 锁定依赖
freeze:
	pip3 list --format=freeze > requirements.txt

# 启动测试
run:
	python3 src/RunAllTests.py
