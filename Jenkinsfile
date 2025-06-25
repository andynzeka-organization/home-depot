pipeline {
    agent any

    environment {
        PYTHON_ENV = 'python3'
    }

    parameters {
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests during the build')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'git@github.com:calekh/Secure-Flow-Interview.git', credentialsId: 'user_ssh_creds'
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (params.RUN_TESTS) {
                        sh '''
                        source venv/bin/activate
                        pytest --maxfail=5 --disable-warnings -q
                        '''
                    } else {
                        echo 'Tests were skipped.'
                    }
                }
            }
        }

        stage('Build Package') {
            steps {
                script {
                    sh '''
                    source venv/bin/activate
                    python -m build
                    '''
                }
            }
        }

        stage('Deploy to Test PyPI') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'test_pypi_credentials', usernameVariable: 'PYPI_USERNAME', passwordVariable: 'PYPI_PASSWORD')]) {
                        sh '''
                        source venv/bin/activate
                        python -m pip install --upgrade twine
                        twine upload --repository-url https://test.pypi.org/legacy/ -u $PYPI_USERNAME -p $PYPI_PASSWORD dist/* --verbose
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'rm -rf venv'
        }

        success {
            echo "Build completed successfully!"
        }

        failure {
            echo "Build failed!"
        }
    }
}