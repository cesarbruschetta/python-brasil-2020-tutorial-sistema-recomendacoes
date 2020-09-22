# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "Ecommerce"
  spec.version       = "0.1.0"
  spec.authors       = ["Cesar Augusto"]
  spec.email         = ["cesarabruschetta@gmail.com"]

  spec.summary       = "Site para vizualização dos produtos e recomendações"
  spec.homepage      = "http://localhost:8080"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass)!i)}

  spec.add_runtime_dependency "jekyll", "~> 4.0"

  spec.add_development_dependency "bundler", "~> 2.1.4"
  spec.add_development_dependency "rake", "~> 12.0"
end
