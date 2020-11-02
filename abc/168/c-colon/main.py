def main():
    import math

    # A: long
    # B: short
    A, B, H, M = map(int, input().split())

    # w: angular velocity
    A_w = 360/(12*60)
    B_w = 360/60

    hour_min = H * 60 + M

    # 角度
    angle = abs(hour_min*A_w - M*B_w)

    # 余弦定理
    # c^2 = a^2+b^2-2ab*cosC
    C_2 = A**2 + B**2 - 2*A*B*(math.cos(math.radians(angle)))
    print(math.sqrt(C_2))


if __name__ == "__main__":
    main()