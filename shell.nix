 let
  jupyter = import (builtins.fetchGit {
    url = https://github.com/tweag/jupyterWith;
    rev = "";
  }) {};

  iPythonWithPackages = jupyter.kernels.iPythonWith {
      name = "datascience";
      packages = p: with p; [
            numpy
            scipy
            pandas
            matplotlib
            seaborn
            umaplearn
            scikitlearn
            ];
      };

  jupyterlabWithKernels = jupyter.jupyterlabWith {
      kernels = [ iPythonWithPackages ];
  };
in
  jupyterlabWithKernels.env
