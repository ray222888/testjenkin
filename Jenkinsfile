node {  
    stage('Build') { 
                echo "checkout from SCM"
                
                git 'https://github.com/webweb04/useful-scripts.git'
                // Make the output directory.
                
                echo "debug"
                sh "mkdir -p output"

                sh "ls -r"


                // Write an useful file, which is needed to be archived.
                writeFile file: "output/usefulfile.txt", text: "This file is useful, need to archive it."

                // Write an useless file, which is not needed to be archived.
                writeFile file: "output/uselessfile.md", text: "This file is useless, no need to archive it."

                echo "Archive build output"

                // Archive the build output artifacts.
                archiveArtifacts artifacts: 'output/*.txt', excludes: 'output/*.md'
    }
    stage('Test') { 
      // sh " echo https://github.com/lzjun567/python_scripts |  /usr/bin/python   02_find_all_links.py >testlog.log"
     //  sh "diff testlog.log reflog.log"
   
     sh "sh ./SUT.sh >testlog.txt "

        sh "cat testlog.txt"
    }
    stage('Deploy') { 
        // 
    }
}
