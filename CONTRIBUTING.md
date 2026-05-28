# Contributing to AI-Powered Business Intelligence Platform

Thank you for your interest in contributing to our project!

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- Git

### Setup Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/jadlidipanshu200-dotcom/AI-Powered-Business-Intelligence-Platform.git
   cd AI-Powered-Business-Intelligence-Platform
   ```

2. **Create .env file**
   ```bash
   cp .env.example .env
   ```

3. **Start with Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **Verify setup**
   ```bash
   curl http://localhost:8000/health
   ```

## Development Workflow

### Creating a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### Branch Naming
- `feature/` - New features
- `bugfix/` - Bug fixes
- `hotfix/` - Hot fixes
- `docs/` - Documentation
- `refactor/` - Code refactoring

### Code Style

#### Python
```bash
cd backend
black src/
isort src/
flake8 src/
```

#### JavaScript/TypeScript
```bash
cd frontend
npm run format
npm run lint:fix
```

### Testing

#### Backend
```bash
cd backend
pytest tests/ -v
```

#### Frontend
```bash
cd frontend
npm test
```

## Pull Request Process

1. **Update your branch**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Push your changes**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request**
   - Clear title and description
   - Reference any related issues
   - Include screenshots for UI changes

4. **Requirements**
   - ✅ All tests pass
   - ✅ No linting errors
   - ✅ Documentation updated
   - ✅ At least 2 approvals

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

### Types
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Formatting
- `refactor` - Code refactoring
- `perf` - Performance
- `test` - Tests
- `chore` - Build/dependencies

### Examples

```bash
git commit -m "feat(auth): add JWT token validation"
git commit -m "fix(dashboard): resolve chart loading issue"
git commit -m "docs: update API documentation"
```

## Documentation

- Keep README.md updated
- Add docstrings to functions
- Update API docs
- Document breaking changes

## Community

- [GitHub Issues](https://github.com/jadlidipanshu200-dotcom/AI-Powered-Business-Intelligence-Platform/issues)
- [GitHub Discussions](https://github.com/jadlidipanshu200-dotcom/AI-Powered-Business-Intelligence-Platform/discussions)

Be respectful and professional in all interactions.

---

Thank you for contributing! 🎉
