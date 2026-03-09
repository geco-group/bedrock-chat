import { BedrockChatParametersInput } from "./lib/utils/parameter-models";

export const bedrockChatParams = new Map<string, BedrockChatParametersInput>();
// You can define multiple environments and their parameters here
// bedrockChatParams.set("dev", {});

// If you define "default" environment here, parameters in cdk.json are ignored
// bedrockChatParams.set("default", {});
bedrockChatParams.set("dev", {
  bedrockRegion: "ap-northeast-1",
  selfSignUpEnabled: false,
  allowedIpV4AddressRanges: ["18.176.40.134/32"], // geco IP address
  enableFrontendIpv6: false, // Disabling this property will still create waf rules to allow ipv6 traffic. Workaround set empty array to disable ipv6 traffic.
  allowedIpV6AddressRanges: [],
  enableRagReplicas: false, // Cost-saving for dev environment
  enableBotStoreReplicas: false, // Cost-saving for dev environment
  titleModel: "claude-v4.6-sonnet",   // Model used for generating conversation titles
  defaultModel: "claude-v4.6-sonnet", // Default model for conversations
  enableBedrockGlobalInference: true,
  globalAvailableModels: ["claude-v4.6-opus", "claude-v4.6-sonnet"]
});
