I have seen some vulnerability like SQL Injection and Cross-site scripting
main/views.py 
 I applied SQL Injection in main/views.py
    cursor.execute(query,[user_input])

I applied Cross-site scripting in  <!-- main/templates/main/vulnerable_template.html -->
wherer safe was replace by escape 
<body>
    <h1>User Input:</h1>
    {{ user_input|}}
</body>

