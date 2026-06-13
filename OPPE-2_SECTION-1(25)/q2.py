def is_dot_com_or_dot_in(domain):
    return(domain.endswith(".com") or domain.endswith(".in"))
    
    
print(is_dot_com_or_dot_in("india.com"))
