

## Project Overview
Gravity is a deep learning framework for aerodynamic and structural physics simulations.

### Surrogate Models
- AeroGNN: Graph Neural Network for aerodynamic surface pressure fields
- StructCNN: Convolutional Neural Network for structural stress distribution
- ThermalPINN: Physics-Informed Neural Network for thermal boundary conditions

### Requirements
- Python 3.10+
- PyTorch 2.0+ with CUDA support
- PyTorch Geometric (PyG)
- SciPy, NumPy, Matplotlib

### Running Benchmarks
```bash
python scripts/evaluate_phase2.py --model aero_gnn --test_cases 100
```

<!-- Mathematical notation verified -->

## License
Apache License 2.0

### Roadmap
- [x] Phase 1: Surrogate baseline models
- [x] Phase 2: Multi-fidelity integration
- [ ] Phase 3: Hardware-accelerated inference deployment

<!-- Enhanced simulation notes -->
