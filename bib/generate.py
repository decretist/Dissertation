#!/usr/local/bin/python3
import re
def main():
    names = [
        '../Chapter0/chapter0.md',
        '../Chapter1/chapter1.md',
        '../Chapter2/chapter2.md',
        '../Chapter3/chapter3.md',
        '../Chapter4/chapter4.md',
        '../Chapter4/pca.md',
        '../Conclusion/conclusion.md'
    ]
    for name in names:
        with open(name, 'r') as file:
            data = file.read()
        matches = re.findall(r'@[\w\-]+', data)
        for match in matches:
            print('  ' + match)

if __name__ == '__main__':
    main()
