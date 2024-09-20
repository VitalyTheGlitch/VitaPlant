from django.db import models


class Category(models.Model):
	name = models.CharField('Название', max_length=50)
	url = models.SlugField('URL', max_length=200, unique=True, default='')
	image = models.ImageField('Фото', null=True, blank=True)
	description = models.TextField('Описание', default='')
	objects = models.Manager()

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''

		return url

class Product(models.Model):
	category = models.ForeignKey(Category, verbose_name='Катерогия товаров', on_delete=models.SET_NULL, null=True)
	name = models.CharField('Название', max_length=200)
	price = models.FloatField('Цена')
	availability = models.BooleanField('В наличии', default=False,null=True, blank=True)
	image = models.ImageField('Фото', null=True, blank=True)
	description = models.TextField('Описание', default='')
	contact = models.TextField('Контакты', default='')
	objects = models.Manager()

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.name

	def is_availible(self):
		return self.availability

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''

		return url

class Pricelist(models.Model):
	name = models.CharField('Название', max_length=200)
	price = models.FloatField('Цена')
	objects = models.Manager()

	class Meta:
		verbose_name = 'Прайс-лист'
		verbose_name_plural = 'Прайс-листы'

	def __str__(self):
		return self.name

class Gallery(models.Model):
	name = models.CharField('Название', max_length=200, default='Фото')
	image = models.ImageField('Фото', null=True, blank=True)
	objects = models.Manager()

	class Meta:
		verbose_name = 'Галерея'
		verbose_name_plural = 'Галереи'

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''

		return url

class SCategory(models.Model):
	name = models.CharField('Название категории', max_length=50)
	url = models.SlugField('URL', max_length=200, unique=True, default='')
	image = models.ImageField('Фото', null=True, blank=True)
	description = models.TextField('Описание', default='')
	objects = models.Manager()

	class Meta:
		verbose_name = 'Категория услуг'
		verbose_name_plural = 'Категории услуг'

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''

		return url

class SProduct(models.Model):
	category = models.ForeignKey(SCategory, verbose_name='Катерогия услуг', on_delete=models.SET_NULL, null=True)
	name = models.CharField('Название услуги', max_length=200)
	price = models.FloatField('Цена')
	image = models.ImageField('Фото', null=True, blank=True)
	description = models.TextField('Описание', default='')
	contact = models.TextField('Контакты', default='')
	objects = models.Manager()

	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'

	def __str__(self):
		return self.name

	def is_availible(self):
		return self.availability

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''

		return url
