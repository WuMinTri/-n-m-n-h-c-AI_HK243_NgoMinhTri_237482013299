
#Ý tưởng 2  chướng ngại vật của 
import numpy as np

DanhSach_Hang_Cot = [(1,1)] #dinh nghia block in chess 

def is_valid_state(state, num_queens):

    return len(state) == num_queens

def get_candidates(state, num_queens):
    
    if not state:
        
        candidates = set(range(num_queens))
        for r_o, c_o in DanhSach_Hang_Cot:
            if r_o == 0: # dong dau
                candidates.discard(c_o)
        return candidates

    position = len(state) # hang dau dat
    candidates = set(range(num_queens)) # cot tiem nang


    for row, col in enumerate(state):
        candidates.discard(col) # del cot co quan haau
        dist = position - row   
        candidates.discard(col + dist) 
        candidates.discard(col - dist) 
    
    
    c_o_xoa_DanhSach_Hang_Cot = set()
    for r_o, c_o in DanhSach_Hang_Cot:
        if r_o == position: # if chuong ngai vat o hang 4
            c_o_xoa_DanhSach_Hang_Cot.add(c_o)
    

    candidates = candidates - c_o_xoa_DanhSach_Hang_Cot
    
    return candidates


def search(state, solutions, num_queens):
    
    if is_valid_state(state, num_queens):
        solutions.append(state.copy()) # ban sao danh sach
        print(f"Tim trang thai hop le: {state}")
        return


    for candidate in get_candidates(state, num_queens):
        state.append(candidate) # clone hau hien tai
        
 
        search(state, solutions, num_queens)
        
     
        print(f"Quay lui tu: {state}")
        state.remove(candidate) 


def solve(num_queens):
    solutions = []
    state = [] # bieu dien cot moi hang
    search(state, solutions, num_queens)
    return solutions

if __name__ == "__main__":
    num_queens = int(input("Nhap so quan hau = "))
    


    solutions = solve(num_queens) 

    if not solutions:
        print("Không tìm thấy giải pháp nào.")
    else:
        for i, solution in enumerate(solutions):
            
            board = np.full((num_queens, num_queens), "-")
            
            
            for row, col in enumerate(solution):
                board[row][col] = 'Q'
            
        
            for r_o, c_o in DanhSach_Hang_Cot:
                if 0 <= r_o < num_queens and 0 <= c_o < num_queens:
                    board[r_o][c_o] = 'X' # chuong ngai vat
            print(f'Giải pháp{solution}')
            print(board)
            print(f"Tổng số giải pháp tìm được của N= {num_queens} là {len(solutions)}")