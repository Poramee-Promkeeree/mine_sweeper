import random

def random_bom(rows: int, cols: int, bom_number: int) -> list:

    mine = []
    newbomb = bom_number
    for row in range(rows):
        row_data = []
        for col in range(cols):
            position = random.randint(0, 1)
            if (rows*cols) > 0:
                row_data.append(0)
                bom_number -= 1 
        mine.append(row_data)
    for x in range(0,len(mine)):
        for i in mine:
            ps = random.randint(0, 1)
            if  ps ==1 and newbomb >0 :
                position1 = random.randint(0, rows-1)
                newbomb -=1
                if i[position1] == 0:
                    i[position1] = -1
                else:
                    newbomb +=1              
    return mine

if __name__ == "__main__":
    mine = random_bom(5,5,5)
    for row in mine:
        print(row)
