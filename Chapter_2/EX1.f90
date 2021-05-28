program lz2.2.5
    implicit none
    
    PARAMETER(IM=102)
    real C(IM), CN(IM), K, DT, DX
    INTEGER I,J,IN

    DX = 100
    DT = 100
    K = 10
    r = K * DT/DX **2

    do I = 1, IM
        C(I) = 0
    enddo
    C(50) = 100

    do 20 IT =1, 1000
        do I =2, IM-1
            CN(I) = (1-2*r) * C(I) + r * C(I+1) + r*C(I-1)
        enddo
        ! 虚拟边界
        CN(1) = CN(2)
        CN(IM) = CN(IM-1)

        do I = 1, IM 
            C(I) = CN(I)
            enddo
    continue

    OPEN(1, FILE = 'concentration.dat')

    DO I = 1, IM 
        write(1,*) I, C(I)
    enddo
    CLOSE(1)

end program lz2.2.5
