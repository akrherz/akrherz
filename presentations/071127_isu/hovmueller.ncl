; ===========================================
; hov_5.ncl
; ===========================================
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
; ===========================================
begin
  f     = addfile ("2006.nc","r")
  d   = f->reflectivity
;==============================================
; create color plot
;=============================================
  wks  = gsn_open_wks ("ps", "hov" )            ; open ps file
  gsn_define_colormap(wks,"BlWhRe")             ; choose colormap

  res                      = True               ; plot mods desired
  res@cnFillOn             = True               ; turn on color fill
  res@gsnSpreadColors      = True               ; use full range of colors

  res@tiMainString         = "Pacific Region"   ; title

  res@cnLevelSelectionMode = "ManualLevels"     ; manual contour levels
  res@cnMinLevelValF       = -10.	        ; min level
  res@cnMaxLevelValF       =  10.               ; max level
  res@cnLevelSpacingF      = 2.                 ; contour level spacing
  
  plot = gsn_csm_hov(wks, d(1:10,:), res) 
  ;plot = gsn_csm_contour(wks, d(1:10,:), res) 
  
end
