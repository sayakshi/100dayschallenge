import os

cur_filepath = os.path.abspath(__file__)
base_dir = os.path.dirname(cur_filepath)
template_dir = os.path.join(base_dir,"template")



class Templates:
	def __init__(self, template_name, context=None, *args, **kwargs):

		self.template_name = template_name
		self.context = context

	def get_template(self):

		template_path = os.path.join(template_dir, self.template_name)
		print(template_path)
		if not os.path.exists(template_path):
			raise Exception("this path doesn't exists")

		read_template = ""
		with open(template_path, 'r') as f:
			read_template = f.read()
		return read_template


	def render(self, context=None):
		render_ctx = {}

		if self.context!=None:
			render_ctx = self.context

		if not isinstance(render_ctx, dict):
			render_ctx = {}
		if context!=None:
			render_ctx = context


	
		print("render_ctx", render_ctx)
		read_template = self.get_template()
		# dictionary unpacking {"a":"b"}==>a=b
		return read_template.format(**render_ctx) 