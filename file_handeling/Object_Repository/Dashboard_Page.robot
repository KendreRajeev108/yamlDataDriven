*** Settings ***
Documentation    Dashboard object repository


*** Variables ***

${search_box}                //input[@placeholder="Search"]
${dashboard}                //*[text()="dashboard"]

${reports}                //*[text()="reports"]
${alerts}                //*[text()="alerts"]
${events}                //*[text()="events"]
${audit_log}                //*[text()="audit log"]

${srvers_title}            //*[text()="servers" and contains(@class,'title')]
${servers_root}            //*[text()="servers" and contains(@class,'root')]
${user_roles}            //*[text()="user roles"]
${failover_groups}        //*[text()="failover groups"]
${licenses}                //*[text()="licenses"]

${cameras_title}            //*[text()="cameras" and contains(@class,'title')]
${cameras_root}            //*[text()="cameras" and contains(@class,'root')]
${inspection}                //*[text()="inspection"]

${web_services}            //*[text()="web services"]
${organization}            //*[text()="organization"]
${users}                    //*[text()="users"]
${groups}                    //*[text()="groups"]
${domain}                    //*[text()="domain"]
${rules_root}                //*[text()="rules" and contains(@class,'title')]
${system}                    //*[text()="system"]

${server_stage}                //*[@id="serverstage"]
${server_stage_chart}    //*[@id="server-stage-chart"]
