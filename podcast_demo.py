from podcastfy.client import generate_podcast
import os
if __name__ == "__main__":


    text = """Istio is an open source service mesh that layers transparently onto existing distributed applications. Istio’s powerful features provide a uniform and more efficient way to secure, connect, and monitor services. Istio is the path to load balancing, service-to-service authentication, and monitoring – with few or no service code changes. It gives you:

    Secure service-to-service communication in a cluster with mutual TLS encryption, strong identity-based authentication and authorization
    Automatic load balancing for HTTP, gRPC, WebSocket, and TCP traffic
    Fine-grained control of traffic behavior with rich routing rules, retries, failovers, and fault injection
    A pluggable policy layer and configuration API supporting access controls, rate limits and quotas
    Automatic metrics, logs, and traces for all traffic within a cluster, including cluster ingress and egress
    Istio is designed for extensibility and can handle a diverse range of deployment needs. Istio’s control plane runs on Kubernetes, and you can add applications deployed in that cluster to your mesh, extend the mesh to other clusters, or even connect VMs or other endpoints running outside of Kubernetes.

    A large ecosystem of contributors, partners, integrations, and distributors extend and leverage Istio for a wide variety of scenarios. You can install Istio yourself, or a large number of vendors have products that integrate Istio and manage it for you.

    How it works
    Istio uses a proxy to intercept all your network traffic, allowing a broad set of application-aware features based on configuration you set.

    The control plane takes your desired configuration, and its view of the services, and dynamically programs the proxy servers, updating them as the rules or the environment changes.

    The data plane is the communication between services. Without a service mesh, the network doesn’t understand the traffic being sent over, and can’t make any decisions based on what type of traffic it is, or who it is from or to.

    Istio supports two data plane modes:

    sidecar mode, which deploys an Envoy proxy along with each pod that you start in your cluster, or running alongside services running on VMs.
    ambient mode, which uses a per-node Layer 4 proxy, and optionally a per-namespace Envoy proxy for Layer 7 features."""

    os.environ['OPENAI_API_KEY'] = 'sk-xxxx'
    os.environ['OPENAI_BASE_URL'] = "http://127.0.0.1:9000/v1"
    # transcript_file = generate_podcast(text=text, tts_model="openai", api_key_label="OPENAI_API_KEY",
    #                               llm_model_name="gpt-4o", transcript_only=True)
    # print(transcript_file)

    text = """
    deepseek，deepseek we're getting our asses kicked by Deepseek who names an AI company after the
thing it actually does 
where are your random letters where's your GPT your Gro deep seek sounds like what you might use it for China is even beating us at naming
    """
    #
    # text = "Deepseek，Deepseek，我们被Deepseek打得落花流水。谁会用一个AI公司实际做的事情来命名公司呢？你们的随机字母在哪里？你们的GPT在哪里？你们的Gro在哪里？Deepseek听起来就像你可能会用到的东西。中国甚至在公司命名上也打败了我们。"

    audio_file = generate_podcast(text=text, tts_model="openai", api_key_label="OPENAI_API_KEY",
                                       llm_model_name="gpt-4o")
    print(audio_file)
