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
  enableRagReplicas: false, // Cost-saving for staging environment
  enableBotStoreReplicas: false, // Cost-saving for staging environment
});
