c ==============
c  Compute the divergence of a regular grid
c  H and u,v are on the same grid
c
      SUBROUTINE DIVG (H, U, V, DHDT, DX, DY, NX, NY)
      INTEGER IX, NX, IY, NY
      REAL*8 U(NX,NY)
      REAL*8 V(NX,NY)
      REAL*8 DHDT(NX,NY)
      REAL*8 H(NX,NY)
      REAL*8 DUDX, DX, DVDY, DY, DIV
cf2py intent(in,out) DHDT

C-------- Solve the divergence term for height tendency


      DO 30 IY = 2, (NY-1)
      DO 20 IX = 2, (NX-1)
         DUDX = (U(IX+1,IY) - U(IX-1,IY)) / (2 * DX)
         DVDY = (V(IX,IY+1) - V(IX,IY-1)) / (2 * DY)
         DIV = H(IX,IY) * (DUDX + DVDY)
         DHDT(IX,IY) = DHDT(IX,IY) - DIV
20    CONTINUE
30    CONTINUE

      RETURN
      END

