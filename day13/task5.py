class Docker:
  def deploy(self):
     print("Docker Deployment")


class Kubernetes:
   def deploy(self):
       print("Kubernetes Deployment")


for tool in (Docker(), Kubernetes()):
   tool.deploy()
