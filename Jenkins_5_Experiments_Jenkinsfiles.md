# Jenkins CI/CD Lab — 5 Pipeline Jenkinsfiles

> Based on the five projects in the ISWE406L lab manual.
>
> **Important:** Replace `YOUR_USERNAME` and `YOUR_REPO` in every Jenkinsfile with your actual GitHub username and repository name.

---

## Experiment 1 — Parameterized Build Pipeline

**Concept:** Jenkins asks for an environment before the pipeline starts.

### Jenkinsfile

```groovy
pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'staging', 'prod'],
            description: 'Select the deployment environment'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Show Parameter') {
            steps {
                echo "Selected environment: ${params.ENVIRONMENT}"
            }
        }

        stage('Build for Environment') {
            steps {
                echo "Building the application for the ${params.ENVIRONMENT} environment..."
            }
        }
    }
}
```

---

## Experiment 2 — Archive Build Artifacts Pipeline

**Concept:** Jenkins saves files produced by a build using `archiveArtifacts`.

### app.py

```python
with open("report.txt", "w") as f:
    f.write("Application Report\n")
    f.write("Total Users: 120\n")
    f.write("Active Sessions: 45\n")

print("Report generated.")
```

### Jenkinsfile

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Generate Report') {
            steps {
                bat 'python app.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.txt',
                              fingerprint: true
            }
        }
    }
}
```

---

## Experiment 3 — Parallel Stages Pipeline

**Concept:** Independent tasks can execute at the same time using `parallel`.

### frontend_check.py

```python
import time

print("Running frontend checks...")
time.sleep(3)
print("Frontend checks passed.")
```

### backend_check.py

```python
import time

print("Running backend checks...")
time.sleep(3)
print("Backend checks passed.")
```

### Jenkinsfile

```groovy
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Parallel Checks') {

            parallel {

                stage('Frontend Check') {
                    steps {
                        bat 'python frontend_check.py'
                    }
                }

                stage('Backend Check') {
                    steps {
                        bat 'python backend_check.py'
                    }
                }
            }
        }

        stage('Summary') {
            steps {
                echo 'Both frontend and backend checks are complete.'
            }
        }
    }
}
```

---

## Experiment 4 — Conditional Stage Execution Pipeline

**Concept:** A stage runs only when a condition is true using the `when` directive.

### app.py

```python
def greet(name):
    return "Hello, " + name
```

### Jenkinsfile

```groovy
pipeline {
    agent any

    parameters {
        booleanParam(
            name: 'RUN_EXTRA_CHECK',
            defaultValue: true,
            description: 'Run the extra check stage?'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'
                echo 'Build successful: app.py compiled with no syntax errors'
            }
        }

        stage('Extra Check') {

            when {
                expression {
                    params.RUN_EXTRA_CHECK == true
                }
            }

            steps {
                echo 'Running extra check: verifying greet() output format...'

                bat 'python -c "from app import greet; print(greet(\'Student\'))"'
            }
        }
    }
}
```

---

## Experiment 5 — Custom Environment Variables Pipeline

**Concept:** User-defined variables are declared in an `environment` block and can be used across stages.

### app.py

```python
def add(a, b):
    return a + b
```

### Jenkinsfile

```groovy
pipeline {
    agent any

    environment {
        APP_NAME = 'GradeBookApp'
        APP_VERSION = '1.0.0'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Show App Info') {
            steps {
                echo "Building ${env.APP_NAME}, version ${env.APP_VERSION}"
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'

                echo "${env.APP_NAME} version ${env.APP_VERSION} compiled successfully."
            }
        }
    }
}
```

---

## Quick Reference

| Experiment | Main Jenkins Feature |
|---|---|
| 1. Parameterized Build | `parameters` |
| 2. Archive Artifacts | `archiveArtifacts` |
| 3. Parallel Stages | `parallel` |
| 4. Conditional Stage | `when` |
| 5. Custom Environment Variables | `environment` |

### Key syntax to remember

```text
Experiment 1 → parameters → params.X
Experiment 2 → archiveArtifacts
Experiment 3 → parallel
Experiment 4 → when
Experiment 5 → environment → env.X
```
