
# Nombre del proyecto:
CoffeeShop

## Descripción del proyecto:
CoffeeShop es una aplicación web django que simula una cafetería en línea donde los usuarios pueden explorar un menú de café y la página de detalles de cada artículo del menú, registrarse, iniciar sesión, agregar artículos a su orden.

#  Estructura del proyecto:
> El proyecto consta de 4 aplicaciones principales:

- Aplicación de usuarios: esta aplicación se encarga de la autenticación y el registro de usuarios. Los usuarios pueden registrarse, iniciar sesión y administrar su página de perfil. El registro se realizará mediante correo electrónico y contraseña, por lo que se requiere personalizar el modelo de usuario y utilizar la clase AbstractUser. Además, cada usuario debe completar el registro mediante la confirmación de correo electrónico en el correo electrónico para activarlo. También se necesita un código OTP para confirmar el número de teléfono móvil del usuario si el usuario elige habilitar la autenticación de dos factores. En esta aplicación, se necesitan señales para enviar un correo electrónico de confirmación mediante uid y token, así como para crear un perfil de usuario.

- Aplicación Páginas: La aplicación Páginas no tiene modelos, solo es responsable de mostrar las páginas principales de la aplicación para los usuarios y el administrador como el índice, acerca de, el panel de administración y el gráfico del panel y otras páginas.

- Aplicación Productos: La aplicación Productos es responsable de toda la actividad relacionada con el producto (café), sirve para mostrar el menú de café y los detalles del café. Incluye las siguientes funciones:

- Todos los productos(productos): Muestra una lista del menú de café que contiene todos los productos con imágenes, nombres, descripciones, precios, número de visitas, me gusta, calificaciones y reseñas.

- Buscar producto: los usuarios pueden buscar productos según el nombre, la descripción, el rango de precios y el buscador puede seleccionar si la búsqueda será sensible o no.





![image](https://github.com/user-attachments/assets/e2d3d168-c9af-4627-9129-03eb85aab625)
![image](https://github.com/user-attachments/assets/a4c3776b-24a8-4152-bd72-e7e940c0557b)


![image](https://github.com/user-attachments/assets/e8937fa8-ea72-44c7-a7dc-b1de1183f20f)

![image](https://github.com/user-attachments/assets/8b11e797-5cdc-4e1f-b612-fae9ba62d537)




### ¿Qué es el Django Admin?
Django Admin es una herramienta integrada en Django que permite administrar modelos y objetos a través de una interfaz web intuitiva y fácil de configurar.

### ¿Cómo accedemos al Django Admin?
Primero, asegúrate de que el proyecto de Django esté corriendo. Luego, accede a la URL “/admin”. Aparecerá una página de inicio de sesión con el título “Django Administration”.

### ¿Cómo creamos un superusuario?
Para acceder al admin, necesitas un superusuario. Detén el servidor y ejecuta el comando createsuperuser. Proporciona un nombre de usuario, correo electrónico y contraseña. Reinicia el servidor y usa estas credenciales para iniciar sesión en el admin.
```
bash
python3 manage.py createsuperuser

Para iniciar sesión en el sitio, ve a la URL /admin (e.j. http://127.0.0.1:8000/admin) e ingresa tus credenciales de id usuario y contraseña de administrador (serás redirigido a la página login, y entonces volverás a la URL de /admin después de haber ingresado tus datos).

python3 manage.py runserver
```

### ¿Cómo registramos un modelo en el Django Admin?
- Abre el archivo admin.py dentro de tu aplicación.
- Crea una nueva clase que herede de admin.ModelAdmin.
- Importa tu modelo con from .models import Product.
- Registra el modelo usando admin.site.register(Product, ProductAdmin).

### ¿Cómo personalizamos la vista de lista en el Django Admin?
Puedes añadir campos a la lista de visualización usando list_display:

```
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
```
Esto muestra los campos name y price en la lista de productos.

### ¿Cómo agregamos funcionalidad de búsqueda?
```
Añade el atributo search_fields en la clase del administrador:

class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
Esto permite buscar productos por nombre.
```
### ¿Cómo editamos y guardamos productos?
Desde la lista de productos, haz clic en un producto para abrir el formulario de edición. Realiza los cambios necesarios y selecciona una de las opciones de guardado.

### Crear users

```
./manage.py startapp users 
```


### ¿Cómo añadimos imágenes a los productos?
- Asegúrate de tener un campo de imagen en tu modelo.
- Sube una imagen a través del formulario de edición.
- Configura las URLs para servir archivos estáticos agregando la configuración en urls.py:
```
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
### ¿Cómo administramos múltiples productos?
Selecciona varios productos usando los checkboxes y aplica acciones en masa, como eliminar.

### ¿Cómo configuramos la visualización de imágenes en la lista de productos?
Configura las URLs de los archivos estáticos y media para que Django sepa dónde encontrarlas. Asegúrate de importar y utilizar correctamente static y settings en tu archivo urls.py.

### ¿Cómo agregamos un nuevo campo al modelo?
Para agregar un nuevo campo, como la fecha de creación, modifica el modelo y actualiza la clase del administrador para mostrarlo en la lista:
```
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
```
### ¿Cómo definimos los modelos?
Después de registrar la aplicación, procedemos a crear los modelos. Iniciamos con el modelo Product que hereda de Model. El primer campo será Name, definido como un TextField con un MaxLength de 200 caracteres.

¿Qué es Verbose Name y cómo lo utilizamos?
El Verbose Name nos permite especificar cómo queremos que se visualice cada campo para el usuario final. Por ejemplo, para Name podemos definir un verbose_name.

¿Qué otros campos añadimos?
Aparte de Name, añadimos otros campos importantes:

Description: TextField con MaxLength de 300.
Price: DecimalField con max_digits de 10 y decimal_places de 2.
Available: BooleanField con default=True.
Photo: ImageField con upload_to='logos', permitiendo valores nulos (null=True) y en blanco (blank=True).
¿Cómo formateamos el código y solucionamos errores de dependencias?
Para mantener el código limpio, utilizamos la extensión Black. Hacemos clic derecho, seleccionamos Format Document Width y elegimos Black Formatter.

Si el editor no encuentra las dependencias, debemos asegurarnos de que Visual Studio Code esté utilizando el entorno virtual correcto. Seleccionamos el entorno correcto en la parte inferior del editor y recargamos la ventana con Command P o Control P seguido de reload window.

¿Cómo añadimos un método str?
Para una representación textual del modelo, añadimos un método __str__ que retorna el nombre del producto.

## `Recursos`

[Tutorial: Implementa un Sistema de Inicio de Sesión en Django 4.1 con Autenticación Integrada](https://www.youtube.com/watch?v=6rMSouSx3II)

Crispy Form Tailwind: https://github.com/django-crispy-forms/crispy-tailwind
