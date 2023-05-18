from django.db import models
from users.models import User

class Tag(models.Model):
    name = models.CharField(
        verbose_name='Тэг',
        max_length=40,
        unique=True,
    )
    color = models.CharField(
        verbose_name='Цвет',
        max_length=7,
        unique=True,
    )
    slug = models.CharField(
        verbose_name='Слаг тэга',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self) -> str:
        return f'{self.name} (цвет: {self.color})'


class Ingredients(models.Model):
    name = models.CharField(
        verbose_name='Ингридиент',
        max_length=100,
    )
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения',
        max_length=24,
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        

    def __str__(self) -> str:
        return f'{self.name} {self.measurement_unit}'



# Create your models here.
class Recipe(models.Model):
    pass
    #сделать поле для юзеров
    author = models.ForeignKey(verbose_name='Автор',related_name='recipe',to=User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(verbose_name='Тег', related_name='recipe', to=Tag)
    title = models.CharField(max_length=50, verbose_name='Название блюда')
    image = models.ImageField(verbose_name='Изображение блюда', upload_to='recipe_images/',)
    ingredient = models.ManyToManyField(verbose_name='Ингридиенты',related_name='recipe', to=Ingredients, through='recipe.AmountIngredient',)
    description = models.TextField(verbose_name='Описание блюда',blank=True)
    tag = models.CharField(max_length=20)
    time_to_done = models.IntegerField(verbose_name='Время приготовления',default=0)
    
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        

    def __str__(self) -> str:
        return f'{self.title}. Автор: {self.author.username}'
    
    
class AmountIngredient(models.Model):
    

    recipe = models.ForeignKey(
        verbose_name='В каких рецептах',
        related_name='ingredients',
        to=Recipe,
        on_delete=models.CASCADE,
    )
    ingredients = models.ForeignKey(
        verbose_name='Связанные ингредиенты',
        related_name='recipes',
        to=Ingredients,
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        verbose_name='Количество',
        default=0,
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Количество ингридиентов'
        

    def __str__(self) -> str:
        return f'{self.amount} {self.ingredients}'



class Favorites(models.Model):
    recipe = models.ForeignKey(
        verbose_name='Понравившиеся рецепты',
        related_name='in_favorites',
        to=Recipe,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        related_name='favorites',
        to=User,
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        editable=False
    )

    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'

    def __str__(self) -> str:
        return f'{self.user} -> {self.recipe}'



class Carts(models.Model):
    recipe = models.ForeignKey(
        verbose_name='Рецепты в списке покупок',
        related_name='in_carts',
        to=Recipe,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        verbose_name='Владелец списка',
        related_name='carts',
        to=User,
        on_delete=models.CASCADE,
    )
    date_added = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        editable=False
    )

    class Meta:
        verbose_name = 'Рецепт в списке покупок'
        verbose_name_plural = 'Рецепты в списке покупок'
        

    def __str__(self) -> str:
        return f'{self.user} -> {self.recipe}'

