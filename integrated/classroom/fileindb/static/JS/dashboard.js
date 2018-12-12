var performancedata = (function() {
    return{
        crossfilter : function(){
            var url =  
            d3.json( 'attendence_data/' , function(error, data) {
            var studentsPerformance = crossfilter(data);

            console.log(data);
            
            // data.forEach(function (d) {
            //     d.total = d.attendence['attendence'] / d.attendence_max;
            //     console.log(d.total);
            // });
            //
            // console.log(data);
            // console.log(data.course_id);
            //  var dim = studentsPerformance.dimension(
            //      function(d){
            //         cal = d.total;
            //          console.log(cal);
            //          if ( cal <= 0.33) return '0-33' ;
            //          if ( cal >0.33 & cal <= 0.7) return '34-70' ;
            //          if ( cal > 0.7) return '71-100' ;
            //      }
            //  );
            //  var attendenceGroup = dim.group();
            // console.log(attendenceGroup.size() + "ads");
            // // var attendencegroup_all = attendence.groupAll();
            // // console.log(attendencegroup_all + "attendencegroup");
            //
            // var body = d3.select('body');
            //
            // var pieChart = dc.pieChart("#attendence");
            // pieChart
            //    .width(800)
            //    .height(300)
            //    .dimension(dim)
            //    .group(attendenceGroup)
            //    .on('renderlet', function(chart) {
            //       chart.selectAll('rect').on('click', function(d) {
            //          console.log('click!', d);
            //       });
            //    });

               
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
                .width(500)
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

            //tag name
            function addtag(){
                data.forEach(function (d) {
                    d.tag = 
                    console.log(d.total);
                });
            }
            
               dc.renderAll();

        });
    }


    }
})(); 