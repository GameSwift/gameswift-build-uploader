# -*- encoding: utf-8 -*-
# stub: net-http-uploadprogress 2.0.0 ruby lib

Gem::Specification.new do |s|
  s.name = "net-http-uploadprogress".freeze
  s.version = "2.0.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["SKAhack".freeze, "Vais Salikhov".freeze]
  s.date = "2015-01-12"
  s.description = "Get the file uploading progress.".freeze
  s.email = ["m@skahack.com".freeze, "vsalikhov@gmail.com".freeze]
  s.homepage = "https://github.com/SKAhack/net-http-uploadprogress".freeze
  s.required_ruby_version = Gem::Requirement.new("~> 2.0".freeze)
  s.rubygems_version = "2.6.14.4".freeze
  s.summary = "Get the file uploading progress.".freeze

  s.installed_by_version = "2.6.14.4" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<minitest>.freeze, [">= 0"])
    else
      s.add_dependency(%q<minitest>.freeze, [">= 0"])
    end
  else
    s.add_dependency(%q<minitest>.freeze, [">= 0"])
  end
end
