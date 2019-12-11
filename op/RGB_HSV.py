def Rgb_convert_Hsv(rgb):
    R,G,B = rgb[0]/255.0,rgb[1]/255.0,rgb[2]/255.0
    max_val = max(R,G,B)
    min_val = min(R,G,B) 
    if (max_val-min_val) != 0:
        if R == max_val:
            H = (G-B)/float(max_val-min_val)
        if G == max_val:
            H = 2 + (B-R)/float(max_val-min_val)
        if B == max_val:
            H = 4 + (R-G)/float(max_val-min_val)

        H = H * 30
        if H < 0:
            H = H + 180
        V=max(R,G,B)
        S=(max_val-min_val)/max_val
        
        HSV_list = []
        HSV_list.append(H)
        HSV_list.append(int(S*255))
        HSV_list.append(int(V*255))
        return HSV_list
    else:
        return [0,0,max_val]
    

print(Rgb_convert_Hsv([200,200,200]))
  
