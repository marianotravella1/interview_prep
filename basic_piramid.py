def build_pramid(base: int) -> None:
    for i in range(base+1):
        for j in range(i):
            print(i, end=" ")
        print()
if __name__ == '__main__':
    build_pramid(5)


