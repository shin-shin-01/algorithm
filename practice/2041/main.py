
def create(block):
    """
    create new block (N^2 * N^2) from old block (N * N)
    """
    block_output = []
    N = len(block)

    for n_x in range(N):
        for n_y in range(N):
                
            b = block[n_y][n_x]
            if b == '#':
                out = block
            else:
                out = [list('.' * N)] * N
            
            for o_idx in range(len(out)):
                idx = N * n_y + o_idx

                if len(block_output) < idx + 1:
                    block_output.append([])
                
                block_output[idx].extend(out[o_idx])
                
    return block_output


def main():
    # init
    K = int(input())
    N = int(input())
    block = []

    for _ in range(N):
        block.append(list(input()))
        
    # create Block
    for _ in range(K):
        block = create(block)

    # output
    for block_x in block:
        print(''.join(block_x))


if __name__ == "__main__":
    main()
