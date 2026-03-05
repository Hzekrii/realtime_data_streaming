# cassandra/cassandra-env.sh

# ✅ Keep LOCAL_JMX behavior but disable authentication
LOCAL_JMX=no

if [ "$LOCAL_JMX" = "yes" ]; then
  JVM_OPTS="$JVM_OPTS -Dcassandra.jmx.local.port=$JMX_PORT"
else
  JVM_OPTS="$JVM_OPTS -Dcom.sun.management.jmxremote.port=$JMX_PORT"
  JVM_OPTS="$JVM_OPTS -Dcom.sun.management.jmxremote.rmi.port=$JMX_PORT"
  JVM_OPTS="$JVM_OPTS -Dcom.sun.management.jmxremote.ssl=false"
  # ✅ KEY FIX: Disable authentication completely
  JVM_OPTS="$JVM_OPTS -Dcom.sun.management.jmxremote.authenticate=false"
  JVM_OPTS="$JVM_OPTS -Djava.rmi.server.hostname=cassandra"
fi