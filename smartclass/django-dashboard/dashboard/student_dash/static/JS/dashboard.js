var performancedata = (function() {
    return{
        crossfilter : function(){
            var url =  
            d3.json( 'attendence_data/' , function(error, data) {
                // console.log(data);
                // attendence_data
                //cleandata(data)

            var studentsPerformance = crossfilter(data);
            
            var attendence = studentsPerformance.dimension(function(d) {
                return d['attendence']['attendence']
            });

            console.log(attendence);
             
            var attendenceGroup = attendence.group();
            console.log(attendenceGroup.size());
            // var attendencegroup_all = attendence.groupAll();
            // console.log(attendencegroup_all + "attendencegroup");
            
            var body = d3.select('body');0

            body.append('h2').text("Attendance");
            
            value_below7 = attendenceGroup.top(1)[0]['key']
            value_above7 = attendenceGroup.top(2)[1]['key']
            console.log("above 7"+ value_above7)
            value_below7_count = attendenceGroup.top(2)[0]['value']
            value_above7_count = attendenceGroup.top(2)[1]['value']


            body.append('h2').text(value_below7 + " count = " + value_below7_count);
            body.append('h2').text(value_above7 + " count = " + value_above7_count);
            
            var count = value_above7_count + value_below7_count; 
            console.log(count)
            attendencepercentage_under7 =  (value_below7_count/count) * 100;
            body.append('h3').text(Math.round(attendencepercentage_under7) + "%")


            var pieChart = dc.pieChart("#attendence");
            pieChart
               .width(800)
               .height(300)
               .dimension(attendence)
               .group(attendenceGroup)
               .on('renderlet', function(chart) {
                  chart.selectAll('rect').on('click', function(d) {
                     console.log('click!', d);
                  });
               });

               
               sid = studentsPerformance.dimension(function(d) {
                return d['student_id']
            });
                var sid_group = sid.group();
                min_sid = sid_group.top(1)[0]['key'];
                size =  sid_group.size();
                max_sid = sid_group.top(size)[ size-2 ][ 'key' ]; //change the rollnumber input
                console.log("siddhant" + min_sid);
                console.log("siddhant" + max_sid);

                var raisedhands = studentsPerformance.dimension(function(d) {
                    return d['marks'];
                });

                console.log(raisedhands);
                var raisedhands_group = raisedhands.group();
                console.log(raisedhands.top(2)[1]);
                console.log(raisedhands_group.top(1)[0]);

                min_ra = raisedhands_group.top(1)[0]['key'];
                size_ra = raisedhands_group.size();
                // max_ra =raisedhands_group.top(size)[]['key'];

                console.log( "as" + "   " + raisedhands_group.top(20)[1]['key']);

                var barChart_all_raisedhands = dc.barChart('#raisedhands');
               barChart_all_raisedhands
                .x(d3.scale.linear().domain([10, 100]))
                .width(700)
                .height(500)
                .dimension(raisedhands)
                .group(raisedhands_group)
                .xAxisLabel('Marks')
                .yAxisLabel('Number of students');

                
                var countChart = dc.dataCount("#mystats");
                countChart
               .dimension(studentsPerformance)
               .group(studentsPerformance.groupAll());

                var tableChart = dc.dataTable("#mytable");
                tableChart
               .dimension(raisedhands)
               .group(function (data) {
                  return raisedhands_group;
               })
               .size(Infinity)
               .columns(['student_id', 'student_name','marks' ])
               .sortBy(function (d) {
                  return d.value;
               })
               .order(d3.ascending);

            dc.renderAll();


        });
    }





    }
})(); 