PARAMETER(IM=102)

real C(IM), CN(IM), K, DT, DX
INTEGER I,J,IN

DX = 100
DT = 100
K = 10
r = K * DT/DX **2

DO I = 1, IM
    C(I) = 0
ENDDO
C(50) = 100

DO 20 IT =1, 1000
    DO I =2, IM-1
        CN(I) = (1-2*r) * C(I) + r * C(I+1) + r*C(I-1)
    ENDDO
    ! 虚拟边界
    CN(1) = CN(2)
    CN(IM) = CN(IM-1)

    DO I = 1, IM 
        C(I) = CN(I)
    ENDDO
Continue

OPEN(1, FILE = 'concentration.dat')

DO I = 1, IM 
    write(1,*) I, C(I)
ENDDO
CLOSE(1)

END

