name-divination
=============
# Introduction
A program that tells fortunes about chemistry between two names (Korean only)
# Requirement
Python 3
# Usage

	$ python name-divination.py
	첫번째 사람의 이름 >> 김수연 
	두번째 사람의 이름 >> 황일환
	======================
	김  황  수  일  연  환
	 7   8   4   7   6   9
	   5   2   1   3   5
	     7   3   4   8
	       0   7   2
	         7   9
	======================
	판정 결과: 79%
	======================

It is still valid if the length of name is longer or shorter than 3. But it is impossible to run with two names whose difference between lengths is 2 or more.