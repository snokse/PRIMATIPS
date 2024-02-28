        if i==0 and j==1:
            label = tk.Label(cadre, text="1",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==2:
            label = tk.Label(cadre, text="X",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==3:
            label = tk.Label(cadre, text="2",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==4:
            label = tk.Label(cadre, text="1X2",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==5:
            label = tk.Label(cadre, text="1X",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==6:
            label = tk.Label(cadre, text="12",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)  
        if i==0 and j==7:
            label = tk.Label(cadre, text="X2",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2) 
        else:
            label = tk.Label(cadre, text=f"{i+1}x{j+1}",
                       relief="groove", borderwidth=10)
            label.grid(row=i, column=j, padx=2, pady=2)