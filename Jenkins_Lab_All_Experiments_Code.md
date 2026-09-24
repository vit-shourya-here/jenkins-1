# Jenkins CI/CD Lab --- Python & Jenkins Pipeline Code

## Experiment 1 --- Build & Test Pipeline

### Experiment Name

**Build & Test Pipeline --- Automated Unit Testing**

### `app.py`

``` python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### `test_app.py`

``` python
from app import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
```

### `requirements.txt`

``` text
pytest
```

### `Jenkinsfile`

``` groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<student-username>/<repo-name>.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest test_app.py'
            }
        }
    }
}
```

------------------------------------------------------------------------

# Experiment 2 --- Parametrized Unit Tests

### Experiment Name

**List Utilities --- Build & Test Pipeline with Parametrized Tests**

### `app.py`

``` python
def find_max(numbers):
    return max(numbers)

def count_evens(numbers):
    return len([n for n in numbers if n % 2 == 0])
```

### `test_app.py`

``` python
import pytest
from app import find_max, count_evens

@pytest.mark.parametrize("numbers, expected", [
    ([1, 5, 3], 5),
    ([-10, -2, -7], -2),
    ([4, 4, 4], 4),
])
def test_find_max(numbers, expected):
    assert find_max(numbers) == expected

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4], 2),
    ([1, 3, 5], 0),
    ([2, 4, 6, 8], 4),
])
def test_count_evens(numbers, expected):
    assert count_evens(numbers) == expected
```

### `requirements.txt`

``` text
pytest
```

### `Jenkinsfile`

``` groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<student-username>/<repo-name>.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest test_app.py -v'
            }
        }
    }
}
```

### If using the user's filenames

If your files are named `test_counting.py` and `requirement.txt`, use:

``` groovy
stage('Dependencies') {
    steps {
        bat 'pip install -r requirement.txt'
    }
}

stage('Test') {
    steps {
        bat 'pytest test_counting.py -v'
    }
}
```

------------------------------------------------------------------------

# Experiment 3 --- Manual Approval Gate

### Experiment Name

**Manual Approval Gate --- Deploy Pipeline**

### `app.py`

``` python
print("Deploying application version 1.0...")
print("Deployment complete.")
```

### `Jenkinsfile`

``` groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<student-username>/<repo-name>.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'
                echo 'Build successful: app.py compiled with no syntax errors'
            }
        }

        stage('Deploy') {
            steps {
                input message: 'Approve deployment to production?', ok: 'Deploy'
                bat 'python app.py'
            }
        }
    }
}
```

------------------------------------------------------------------------

# Experiment 4 --- Environment Variables and Linting

### Experiment Name

**Environment Variables + Linting Pipeline**

### `app.py`

``` python
def greet(name):
    return "Hello, " + name
```

### `Jenkinsfile`

``` groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<student-username>/<repo-name>.git'
            }
        }

        stage('Show Build Info') {
            steps {
                echo "Build Number: ${env.BUILD_NUMBER}"
                echo "Job Name: ${env.JOB_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
            }
        }

        stage('Run Linter') {
            steps {
                bat 'flake8 app.py'
            }
        }
    }
}
```

------------------------------------------------------------------------

# Experiment 5 --- Post-Build Success/Failure

### Experiment Name

**Post-Build Success/Failure Pipeline**

### `app.py`

``` python
def multiply(a, b):
    return a * b

print(multiply(4, 5))
```

### `Jenkinsfile`

``` groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<student-username>/<repo-name>.git'
            }
        }

        stage('Compile Check') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }
    }

    post {
        success {
            echo 'Build succeeded: app.py has no syntax errors.'
        }

        failure {
            echo 'Build failed: check app.py for syntax errors.'
        }
    }
}
```

------------------------------------------------------------------------

# Experiment 6 --- Email Notification

### Experiment Name

**Jenkins Pipeline Email Notification**

### `app.py`

``` python
def add(a, b):
    return a + b
```

### `Jenkinsfile`

``` groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<student-username>/<repo-name>.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'
                echo 'Build successful: app.py compiled with no syntax errors'
            }
        }

        stage('Send Notification') {
            steps {
                mail to: 'student@example.com',
                     cc: 'instructor@example.com',
                     subject: "Build Notification: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     body: "The build for ${env.JOB_NAME} has completed.\n\nCheck it here: ${env.BUILD_URL}"
            }
        }
    }
}
```

### Classroom alternative when SMTP is not configured

``` groovy
stage('Send Notification') {
    steps {
        echo "EMAIL WOULD BE SENT -> To: student@example.com | Subject: Build Notification: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
    }
}
```

------------------------------------------------------------------------

# Experiment 7 --- Milestone Step

### Experiment Name

**Jenkins Pipeline Milestone --- Handling Overlapping Builds**

### `app.py`

``` python
def add(a, b):
    return a + b
```

### `Jenkinsfile`

``` groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<student-username>/<repo-name>.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile app.py'
                milestone(1)
                echo 'Build stage passed milestone 1'
            }
        }

        stage('Deploy') {
            steps {
                milestone(2)
                echo 'Deploying application...'
            }
        }
    }
}
```

### Milestone demonstration version

Use this version if you need to demonstrate overlapping builds:

``` groovy
stage('Build') {
    steps {
        bat 'python -m py_compile app.py'
        sleep(time: 15, unit: 'SECONDS')
        milestone(1)
        echo 'Build stage passed milestone 1'
    }
}
```

Then click **Build Now twice quickly**. The newer build can pass the
milestone first; when the older build later reaches that same milestone,
Jenkins aborts the older build.

------------------------------------------------------------------------

# Common Jenkins Pipeline Template

Use this structure to remember the basic syntax:

``` groovy
pipeline {
    agent any

    stages {
        stage('Stage Name') {
            steps {
                // commands
            }
        }

        stage('Another Stage') {
            steps {
                // commands
            }
        }
    }

    post {
        success {
            // runs after a successful pipeline
        }

        failure {
            // runs after a failed pipeline
        }
    }
}
```

# Common Commands Used

### Install Python requirements

``` groovy
bat 'pip install -r requirements.txt'
```

### Compile Python code

``` groovy
bat 'python -m py_compile app.py'
```

### Run pytest

``` groovy
bat 'pytest test_app.py'
```

### Run pytest verbosely

``` groovy
bat 'pytest test_app.py -v'
```

### Run flake8

``` groovy
bat 'flake8 app.py'
```

### Print information

``` groovy
echo 'Hello'
```

### Pause for manual approval

``` groovy
input message: 'Approve deployment?', ok: 'Deploy'
```

### Milestone

``` groovy
milestone(1)
```

### Sleep

``` groovy
sleep(time: 15, unit: 'SECONDS')
```

# Experiment Names --- Quick Revision

1.  **Build & Test Pipeline --- Automated Unit Testing**
2.  **List Utilities --- Build & Test Pipeline with Parametrized Tests**
3.  **Manual Approval Gate --- Deploy Pipeline**
4.  **Environment Variables + Linting Pipeline**
5.  **Post-Build Success/Failure Pipeline**
6.  **Jenkins Pipeline Email Notification**
7.  **Jenkins Pipeline Milestone --- Handling Overlapping Builds**
